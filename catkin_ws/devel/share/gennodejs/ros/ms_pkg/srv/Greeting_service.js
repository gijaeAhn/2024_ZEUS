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

class Greeting_serviceRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.action = null;
      this.image_path = null;
      this.user_prompt = null;
    }
    else {
      if (initObj.hasOwnProperty('action')) {
        this.action = initObj.action
      }
      else {
        this.action = '';
      }
      if (initObj.hasOwnProperty('image_path')) {
        this.image_path = initObj.image_path
      }
      else {
        this.image_path = '';
      }
      if (initObj.hasOwnProperty('user_prompt')) {
        this.user_prompt = initObj.user_prompt
      }
      else {
        this.user_prompt = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Greeting_serviceRequest
    // Serialize message field [action]
    bufferOffset = _serializer.string(obj.action, buffer, bufferOffset);
    // Serialize message field [image_path]
    bufferOffset = _serializer.string(obj.image_path, buffer, bufferOffset);
    // Serialize message field [user_prompt]
    bufferOffset = _serializer.string(obj.user_prompt, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Greeting_serviceRequest
    let len;
    let data = new Greeting_serviceRequest(null);
    // Deserialize message field [action]
    data.action = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [image_path]
    data.image_path = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [user_prompt]
    data.user_prompt = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.action);
    length += _getByteLength(object.image_path);
    length += _getByteLength(object.user_prompt);
    return length + 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ms_pkg/Greeting_serviceRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '75a78b45ce12ca215b0b79c78a48ca4d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string action
    string image_path
    string user_prompt
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Greeting_serviceRequest(null);
    if (msg.action !== undefined) {
      resolved.action = msg.action;
    }
    else {
      resolved.action = ''
    }

    if (msg.image_path !== undefined) {
      resolved.image_path = msg.image_path;
    }
    else {
      resolved.image_path = ''
    }

    if (msg.user_prompt !== undefined) {
      resolved.user_prompt = msg.user_prompt;
    }
    else {
      resolved.user_prompt = ''
    }

    return resolved;
    }
};

class Greeting_serviceResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.result = null;
    }
    else {
      if (initObj.hasOwnProperty('result')) {
        this.result = initObj.result
      }
      else {
        this.result = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Greeting_serviceResponse
    // Serialize message field [result]
    bufferOffset = _serializer.string(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Greeting_serviceResponse
    let len;
    let data = new Greeting_serviceResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.result);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ms_pkg/Greeting_serviceResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c22f2a1ed8654a0b365f1bb3f7ff2c0f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string result
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Greeting_serviceResponse(null);
    if (msg.result !== undefined) {
      resolved.result = msg.result;
    }
    else {
      resolved.result = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: Greeting_serviceRequest,
  Response: Greeting_serviceResponse,
  md5sum() { return 'f58cc1930ee734da0da3606508759ab9'; },
  datatype() { return 'ms_pkg/Greeting_service'; }
};
