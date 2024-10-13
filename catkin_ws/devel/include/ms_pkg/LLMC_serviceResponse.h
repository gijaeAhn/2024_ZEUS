// Generated by gencpp from file ms_pkg/LLMC_serviceResponse.msg
// DO NOT EDIT!


#ifndef MS_PKG_MESSAGE_LLMC_SERVICERESPONSE_H
#define MS_PKG_MESSAGE_LLMC_SERVICERESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ms_pkg
{
template <class ContainerAllocator>
struct LLMC_serviceResponse_
{
  typedef LLMC_serviceResponse_<ContainerAllocator> Type;

  LLMC_serviceResponse_()
    : result()  {
    }
  LLMC_serviceResponse_(const ContainerAllocator& _alloc)
    : result(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _result_type;
  _result_type result;





  typedef boost::shared_ptr< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> const> ConstPtr;

}; // struct LLMC_serviceResponse_

typedef ::ms_pkg::LLMC_serviceResponse_<std::allocator<void> > LLMC_serviceResponse;

typedef boost::shared_ptr< ::ms_pkg::LLMC_serviceResponse > LLMC_serviceResponsePtr;
typedef boost::shared_ptr< ::ms_pkg::LLMC_serviceResponse const> LLMC_serviceResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator1> & lhs, const ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator2> & rhs)
{
  return lhs.result == rhs.result;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator1> & lhs, const ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ms_pkg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c22f2a1ed8654a0b365f1bb3f7ff2c0f";
  }

  static const char* value(const ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc22f2a1ed8654a0bULL;
  static const uint64_t static_value2 = 0x365f1bb3f7ff2c0fULL;
};

template<class ContainerAllocator>
struct DataType< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ms_pkg/LLMC_serviceResponse";
  }

  static const char* value(const ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string result\n"
;
  }

  static const char* value(const ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct LLMC_serviceResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ms_pkg::LLMC_serviceResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MS_PKG_MESSAGE_LLMC_SERVICERESPONSE_H
