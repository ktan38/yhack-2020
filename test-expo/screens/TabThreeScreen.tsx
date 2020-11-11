import * as React from 'react';
import { StyleSheet, TouchableOpacity } from 'react-native';

import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';
import Constants from "expo-constants";
// import console = require('console');
const { manifest } = Constants;

const api = (typeof manifest.packagerOpts === `object`) && manifest.packagerOpts.dev
  ? manifest.debuggerHost.split(`:`).shift().concat(`:3000`)
  : `api.something.com`;

console.log("api", api);


export default function TabThreeScreen() {

  function test_request (e) {
    console.log('wowwwwWWWWWWWWWWWW!!!!!!');
    e.preventDefault();
    fetch("192.168.1.8:3000", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        test_input: "Hello!",
      })
    })
    .then((res) => {
        console.log("response: ", res);
        res.json();
    })
    .then((json) => {
        // console.log(json);
        if (json.success) {
            console.log('success!!');
        } else {
            console.log('nota success!');
        }
    })
    .catch((err) => {
        console.log("Err: ", err)
    });
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Nice Three</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      {/* <EditScreenInfo path="/screens/TabTwoScreen.js" /> */}
      <TouchableOpacity onPress={test_request}>
        <Text>Test Fetch Request </Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
