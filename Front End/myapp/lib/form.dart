import 'package:flutter/material.dart';

class InputForm extends StatefulWidget {
  InputForm({Key key}) : super(key : key);

  @override
  _FormProperties createState() => _FormProperties();
}

class _FormProperties extends State<InputForm>
{
  @override
  Widget build(BuildContext context)
  {
    return Form(
      autovalidate: true,
      child: Column(
        children: <Widget>[
          TextFormField(
            decoration: const InputDecoration(
              labelText: 'Name *'
            ),
          ),
          RaisedButton(
            onPressed: null,
            child: Text("Submit"),
          )
        ],
      )
    );
  }
}