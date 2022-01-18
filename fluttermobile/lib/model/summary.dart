class NSummary{
  String ns_content;

  NSummary(this.ns_content);

  factory NSummary.fromJason(Map<String, dynamic> json){
    return NSummary{
      ns_content: json['ns_content']
    };
  }

  dynamic toJson => {
    'ns_content': ns_content,
  };

}