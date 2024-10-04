// Auto-generated. Do not edit!

// (in-package ms_pkg.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class LLMC_serviceRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.user_text = null;
    }
    else {
      if (initObj.hasOwnProperty('user_text')) {
        this.user_text = initObj.user_text
      }
      else {
        this.user_text = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LLMC_serviceRequest
    // Serialize message field [user_text]
    bufferOffset = _serializer.string(obj.user_text, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LLMC_serviceRequest
    let len;
    let data = new LLMC_serviceRequest(null);
    // Deserialize message field [user_text]
    data.user_text = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.user_text);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ms_pkg/LLMC_serviceRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2e0d533caaa6c5a0bfe0e685b3eecbc0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string user_text
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new LLMC_serviceRequest(null);
    if (msg.user_text !== undefined) {
      resolved.user_text = msg.user_text;
    }
    else {
      resolved.user_text = ''
    }

    return resolved;
    }
};

class LLMC_serviceResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.model_text = null;
    }
    else {
      if (initObj.hasOwnProperty('model_text')) {
        this.model_text = initObj.model_text
      }
      else {
        this.model_text = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LLMC_serviceResponse
    // Serialize message field [model_text]
    bufferOffset = _serializer.string(obj.model_text, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LLMC_serviceResponse
    let len;
    let data = new LLMC_serviceResponse(null);
    // Deserialize message field [model_text]
    data.model_text = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.model_text);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ms_pkg/LLMC_serviceResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4ff994df74a709b17eb907236c109202';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string model_text
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new LLMC_serviceResponse(null);
    if (msg.model_text !== undefined) {
      resolved.model_text = msg.model_text;
    }
    else {
      resolved.model_text = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: LLMC_serviceRequest,
  Response: LLMC_serviceResponse,
  md5sum() { return 'c855b39a90951aa6be44ba4ed4e45902'; },
  datatype() { return 'ms_pkg/LLMC_service'; }
};
