import 'package:flutter/material.dart';

import './products.dart';

class ProductCreate extends StatefulWidget {
  final List<String> StartingProducts;

  ProductCreate(this.StartingProducts);

  @override
  State<StatefulWidget> createState() {
    return _ProductManager();
  }
}

class _ProductManager extends State<ProductCreate> {
  List<String> products = [];

  @override
  void initState() {
    products = widget.StartingProducts;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          margin: EdgeInsets.all(10.0),
          child: RaisedButton(
            child: Text("Hello World"),
            color: Colors.blue,
            onPressed: () {
              setState(() {
                products.add("Advanced Camera Icon");
              });
            },
          ),
        ),
        Products(products),
      ], // end children
    );
  }
}
