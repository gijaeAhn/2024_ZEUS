// Generated by gencpp from file ms_pkg/TF_service.msg
// DO NOT EDIT!


#ifndef MS_PKG_MESSAGE_TF_SERVICE_H
#define MS_PKG_MESSAGE_TF_SERVICE_H

#include <ros/service_traits.h>


#include <ms_pkg/TF_serviceRequest.h>
#include <ms_pkg/TF_serviceResponse.h>


namespace ms_pkg
{

struct TF_service
{

typedef TF_serviceRequest Request;
typedef TF_serviceResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct TF_service
} // namespace ms_pkg


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::ms_pkg::TF_service > {
  static const char* value()
  {
    return "05354734935e371f83dc4d09f1c13d77";
  }

  static const char* value(const ::ms_pkg::TF_service&) { return value(); }
};

template<>
struct DataType< ::ms_pkg::TF_service > {
  static const char* value()
  {
    return "ms_pkg/TF_service";
  }

  static const char* value(const ::ms_pkg::TF_service&) { return value(); }
};


// service_traits::MD5Sum< ::ms_pkg::TF_serviceRequest> should match
// service_traits::MD5Sum< ::ms_pkg::TF_service >
template<>
struct MD5Sum< ::ms_pkg::TF_serviceRequest>
{
  static const char* value()
  {
    return MD5Sum< ::ms_pkg::TF_service >::value();
  }
  static const char* value(const ::ms_pkg::TF_serviceRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::ms_pkg::TF_serviceRequest> should match
// service_traits::DataType< ::ms_pkg::TF_service >
template<>
struct DataType< ::ms_pkg::TF_serviceRequest>
{
  static const char* value()
  {
    return DataType< ::ms_pkg::TF_service >::value();
  }
  static const char* value(const ::ms_pkg::TF_serviceRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::ms_pkg::TF_serviceResponse> should match
// service_traits::MD5Sum< ::ms_pkg::TF_service >
template<>
struct MD5Sum< ::ms_pkg::TF_serviceResponse>
{
  static const char* value()
  {
    return MD5Sum< ::ms_pkg::TF_service >::value();
  }
  static const char* value(const ::ms_pkg::TF_serviceResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::ms_pkg::TF_serviceResponse> should match
// service_traits::DataType< ::ms_pkg::TF_service >
template<>
struct DataType< ::ms_pkg::TF_serviceResponse>
{
  static const char* value()
  {
    return DataType< ::ms_pkg::TF_service >::value();
  }
  static const char* value(const ::ms_pkg::TF_serviceResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MS_PKG_MESSAGE_TF_SERVICE_H
