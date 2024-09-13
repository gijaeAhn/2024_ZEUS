import rospy


class EasyLogger():
    def __init__(self, node_name, config, topic_name=None, service_name=None, action_name=None):

        self.node_name =node_name
        self.topic_name = topic_name
        self.action_name = action_name
        self.service_name = service_name

        self.config = config
    

    def initHello(self):
        print("")
        print("")
        rospy.loginfo(f"##############Nodeinfo:::{self.node_name}##################")
        for key in self.config.keys():
            rospy.loginfo(f"{key} -> {self.config[key]} ({type(self.config[key])})")
        rospy.loginfo(f"################################")

        rospy.loginfo(f"{self.node_name} is activated")
        print("")
        print("")


    # def node_log(self, content, prefix='', suffix=''):
    #     rospy.loginfo(prefix + f"Node->{self.node_name}:{content}" + suffix)

    # def topic_log(self, content, prefix='', suffix=''):
    #     if self.topic_name is not None:
    #         rospy.loginfo(prefix + f"Node->{self.node_name}|| Topic-> {self.topic_name}:{content}" + suffix)
    #     else:
    #         raise Exception(f"There is no topic name")
    # def servie_log(self, content, prefix='', suffix=''):
    #     if self.servie_name is not None:
    #         rospy.loginfo(prefix + f"Node->{self.node_name}|| Service-> {self.topic_name}:{content}" + suffix)
    #     else:
    #         raise Exception(f"There is no servie name")
    # def action_log(self, content, prefix='', suffix=''):
    #     if self.action_name is not None:
    #         rospy.loginfo(prefix + f"Node->{self.node_name}|| Action-> {self.topic_name}:{content}" + suffix)
    #     else:
    #         raise Exception(f"There is no action name")
        
    

