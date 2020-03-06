import 'package:flutter/material.dart';

main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Test123'),
        ),
        body: Column(      
          children: [ 
            Container(
              margin: EdgeInsets.all(10.0),
              child:
                RaisedButton(
                child: 
                  Text("Hello World"), 
                  onPressed: (){},
              ),
            ),
            
            Card(
                child: Column(children: <Widget>[
                  Image.asset('assets/camera.png'),
                  Text('Camera Icon')
            ],
            ),),
          ] // end child
        ),
      ),
    );
  }
}
