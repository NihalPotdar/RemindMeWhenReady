import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';
import 'package:http/http.dart' as http;
import 'dart:io';
import 'dart:convert';
import 'package:image_picker/image_picker.dart';

class Button extends StatefulWidget{
  @override
  State<StatefulWidget> createState() {
    return RaiseButton();
  }
}

class RaiseButton extends State<Button>
{
  File _image;

  @override
  Widget build(BuildContext context) {
      return Column( 
        children: [
          RaisedButton(
              child: Text("Hello World"),
              color: Colors.orange,
              splashColor: Colors.deepOrange,
              onPressed: () async {
              //  print( await convertToBase64("nihal", "Test") );
                await getImageTest();
                if(_image != null)
                  print(base64.encode(await _image.readAsBytes()));
              }
          ),
          Center(
            child: _image == null ? Text("No Image Selected") : Image.file(_image)
          )
        ]
      );
    }

    Future getImageTest() async {
      var image = await ImagePicker.pickImage(source: ImageSource.gallery);

      setState(() {
        _image = image;
      });
    }

    // get the documents directory of the phone
    Future<String> get _localPath async {
      final directory = await getApplicationDocumentsDirectory(); 
      print(directory);
      return directory.path;
    }

    // get a file in the documents directory
    Future<dynamic> localFile(final String fileName) async {
      final path = await _localPath;
      return File('$path/$fileName').readAsBytes();
    } 

    Future<dynamic> readFromGallery() async {

    }

    // use the bytes in the file and convert to base 64
    Future<dynamic> convertToBase64(final String name, final dynamic fileRead) async
    {
     // dynamic bs64Values = base64.encode(fileRead);
      var client = http.Client();
      try {
        var response = await client.post( 'https://enmzf4e2nlb5.x.pipedream.net', body: {'name': name, 'image_stream': fileRead} );
        print('Response Status: ${response.statusCode}');
      } finally {
        client.close();
      }
      return 1;
    }
}