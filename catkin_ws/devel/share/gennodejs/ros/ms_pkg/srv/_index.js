
"use strict";

let STT_service = require('./STT_service.js')
let IC_service = require('./IC_service.js')
let LLMC_service = require('./LLMC_service.js')
let Greeting_service = require('./Greeting_service.js')
let TF_service = require('./TF_service.js')
let FER_service = require('./FER_service.js')
let TTS_service = require('./TTS_service.js')

module.exports = {
  STT_service: STT_service,
  IC_service: IC_service,
  LLMC_service: LLMC_service,
  Greeting_service: Greeting_service,
  TF_service: TF_service,
  FER_service: FER_service,
  TTS_service: TTS_service,
};
