import 'package:flutter/material.dart';
import './product_manager.dart';
import './flutter_button.dart';

main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  final List<String> products = ["Nixon Camera", "nikon camera"];
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Test123'),
        ),
       // body: ProductCreate(products),
       body: Container(
         child:
          Button(),
       ),
      ),
    );
  }
}
