import 'package:flutter/material.dart';
import 'root_app.dart';
import 'dart:io';
import 'package:provider/provider.dart';
import '../constants.dart';
import 'package:flutter_svg/flutter_svg.dart';

class StopWatchPage extends StatefulWidget {
  @override
  _StopWatchPageState createState() => _StopWatchPageState();
}

class _StopWatchPageState extends State<StopWatchPage> {
  bool startIsPressed = false;
  bool lapIsPressed = false;
  @override
  Widget build(BuildContext context) {
    var size = MediaQuery.of(context).size;
    return Column(
      children: [
        SizedBox(height: 70),
        Center(
          child: Column(
            children: [
              Text(
                '00 : 00 : 00',
                style: TextStyle(
                  fontSize: 50,
                  color: colors[theme]['clight'],
                  fontWeight: FontWeight.w400,
                ),
              ),
              SizedBox(height: 20),
              Text(
                'TOTAL TIME',
                style: TextStyle(
                  fontSize: 20,
                  color: colors[theme]['clight'],
                  fontWeight: FontWeight.w400,
                ),
              ),
              SizedBox(height: 350),
              Padding(
                padding: const EdgeInsets.only(left: 10, right: 10),
                child: Row(
                  children: [
                    ConstrainedBox(
                      constraints: BoxConstraints.tightFor(
                          width: size.width * 0.4, height: 50),
                      child: ElevatedButton(
                        style: ElevatedButton.styleFrom(
                            primary: colors[theme]['caccent'],
                            shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(100))),
                        onPressed: () {
                          setState(() {
                            if (startIsPressed == false) {
                              startIsPressed = true;
                              lapIsPressed = true;
                            } else {
                              startIsPressed = false;
                              lapIsPressed = false;
                            }
                          });
                        },
                        child: Text(
                          startIsPressed == false ? 'START' : 'PAUSE',
                          style: TextStyle(
                            color: colors[theme]['cback'],
                            fontSize: 16,
                            letterSpacing: 2,
                          ),
                        ),
                      ),
                    ),
                    Expanded(child: Container()),
                    ConstrainedBox(
                      constraints: BoxConstraints.tightFor(
                          width: size.width * 0.4, height: 50),
                      child: ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          primary: colors[theme]['clight'],
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(100)),
                        ),
                        onPressed: () {
                          setState(() {});
                        },
                        child: Text(
                          lapIsPressed == false ? 'CLEAR' : 'REST',
                          style: TextStyle(
                            color: colors[theme]['cback'],
                            fontSize: 16,
                            letterSpacing: 2,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              )
            ],
          ),
        )
      ],
    );
  }
}
