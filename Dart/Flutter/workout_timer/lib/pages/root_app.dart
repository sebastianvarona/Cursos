import 'package:flutter/material.dart';
import 'package:workout_timer/pages/stopwatch.dart';
import 'dart:ui';
import '../constants.dart';
import 'package:provider/provider.dart';
import 'package:stop_watch_timer/stop_watch_timer.dart';
import 'package:flutter_svg/flutter_svg.dart';

class RootApp extends StatefulWidget {
  @override
  _RootAppState createState() => _RootAppState();
}

class _RootAppState extends State<RootApp> {
  int activePage = 1;
  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.only(top: 20),
      decoration: BoxDecoration(
        image: DecorationImage(
            image: AssetImage('assets/fondo.png'), fit: BoxFit.fill),
      ),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: getAppBar(theme),
        body: getBody(activePage),
      ),
    );
  }
}

getAppBar(theme) {
  return AppBar(
    brightness: Brightness.dark,
    backgroundColor: Colors.transparent,
    elevation: 0,
    title: Row(children: [
      RichText(
          text: TextSpan(
        text: 'WORK',
        style: TextStyle(
          fontFamily: 'Montserrat',
          fontWeight: FontWeight.w600,
          fontSize: 20,
          letterSpacing: 2,
          color: colors[theme]['caccent'],
        ),
        children: [
          TextSpan(
            text: 'OUT',
            style: TextStyle(
              fontFamily: 'Montserrat',
              fontWeight: FontWeight.w400,
              letterSpacing: 2,
              color: colors[theme]['clight'],
            ),
          ),
        ],
      )),
      SizedBox(width: 20),
      Text(
        'TIMER',
        style: TextStyle(
            fontWeight: FontWeight.w400,
            letterSpacing: 2,
            color: colors[theme]['cback']),
      ),
    ]),
  );
}

getBody(e) {
  Map pages = {
    1: StopWatchPage(),
    2: null,
  };
  return pages[e];
}
