import 'package:flutter/material.dart';
import 'package:fluttermobile/providers/task_provier.dart';
import 'package:provider/provider.dart';

class NewsTab extends StatelessWidget {
  

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Consumer<NewsProvider>(
        builder: (context, value, child) => NewsList(
          news: value.allSummary),
        ),
    );
  }
}