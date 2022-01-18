import 'package:flutter/material.dart';
import 'package:fluttermobile/providers/task_provier.dart';
import 'package:fluttermobile/screens/home.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(NewsApp());
}

class NewsApp extends StatelessWidget {


  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      builder: (context) => NewsProvider,
      child: MaterialApp(
      title: 'SSG',
      home: HomeScreen(),
      ),
    );
  }
}



