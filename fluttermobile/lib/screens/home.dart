import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> 
with SingleTickerProviderStateMixin {
  late TabController controller;
  @override
  void initState(){
    super.initState();
    controller = TabController(length: 1, vsync: this);
  }
    
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar
        (title: Text('SGG 세줄요약'),
      actions: <Widget>[
        IconButton(
          icon: Icon(Icons.add),
          onPressed: () {}, ),
      ],
      bottom: TabBar(
        controller: controller,
        tabs: <Widget>[
          Tab(icon: Icon(Icons.audiotrack), text: '뉴스'),
        ],
        ),
      ),
      body: TabBarView(
        controller: controller,
        children: <Widget>[
          NewsTab(),
        ],
        ),
    );
  }
}