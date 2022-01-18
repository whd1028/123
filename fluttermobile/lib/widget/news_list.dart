import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:fluttermobile/model/summary.dart';

class NewsList extends StatelessWidget {
  
  final List<NSummary> summary;
  NewsList({required this.summary});

  @override
  Widget build(BuildContext context) {
    return ListView(
      children: getChildrenSolutions(),
    );
  }

  List<Widget> getChildrenSolutions() {
    return summary.map((Summary) => SummaryListItem(summary: summary)).todo
  }
}

