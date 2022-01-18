
import 'dart:collection';
import 'dart:convert';
import 'package:/http/http.dart' as http;
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:fluttermobile/model/summary.dart';

class NewsProvider extends ChangeNotifier{

  List<Summary> _summarys = [];
  UnmodifiableListView(Summary) get allSummary =>
    UnmodifiableListView(_summarys);
  fetchSolutions() async{
    final response = await http.get("http://10.0.2.2:8000/news");
    if (response.statusCode == 200){
      var data = jsonDecode(utf8.decode(response.bodyBytes)) as List;
      _summarys = data.map<Summary>((json)) => Summary.fromJason(json);).toList();

    }
  }
}
