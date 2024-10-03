import insightface
from insightface.app import FaceAnalysis
import numpy as np
import cv2


class FaceAligner():
    def __init__(self, result_size =512):
        self.app = FaceAnalysis(name='buffalo_l')
        self.app.prepare(ctx_id=0, det_size=(640, 640))
        self.crop_ratio = 2
        self.result_size = 512

    def get_face(self, arr):
        faces = self.app.get(arr)
        if faces:
            face = faces[0]
            landmarks = face.landmark_2d_106
            return True, landmarks
        else:
            return False, None
        
    def align(self, arr, lmk_pts):
        center_pt = (lmk_pts[72]+9*lmk_pts[86])/10
        y_basis = lmk_pts[73]-lmk_pts[74]
        y_basis = y_basis/ np.linalg.norm(y_basis)
        x_basis = np.matmul(np.array([[0.0, -1.0],[1.0, 0.0]]),y_basis)
        basis_len = np.linalg.norm(lmk_pts[81]-lmk_pts[75])

        corner0 = center_pt+ self.crop_ratio*basis_len*(-x_basis + y_basis)
        corner1 = center_pt+  self.crop_ratio*basis_len*(x_basis + y_basis)
        corner2 = center_pt+ self.crop_ratio*basis_len*(x_basis - y_basis)
        corner3 = center_pt+ self.crop_ratio*basis_len*(-x_basis - y_basis)
        corners = np.array([corner0, corner1, corner2, corner3], dtype=np.float32)

        dst = np.array([
            [0, 0],
            [self.result_size - 1, 0],
            [self.result_size - 1, self.result_size - 1],
            [0, self.result_size - 1]], dtype="float32")
        M = cv2.getPerspectiveTransform(corners, dst)
        return  cv2.warpPerspective(arr, M, (self.result_size, self.result_size))

    def get_aligned_face(self, img_arr, ):
        face_bool, landmarks = self.get_face(img_arr)
        if face_bool:
            aligned_face_arr = self.align(img_arr, landmarks)
            return face_bool, aligned_face_arr
        else:
            print("here is no face")
            return face_bool, None

