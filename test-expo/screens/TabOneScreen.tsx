import * as React from 'react';
import { StyleSheet, Image, TouchableOpacity, SafeAreaView, Button, Platform, StatusBar } from 'react-native';


import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';

export default function TabOneScreen() {
  return (
    <SafeAreaView style={styles.container}>
      <SafeAreaView style={{
        backgroundColor: "#626FB2",
        flex: 0.25,
        //top: 30,
      }}>
      </SafeAreaView>
      <SafeAreaView style={{
        backgroundColor: "#565EB2",
        flex: 0.7,
      }}>
        <TouchableOpacity onPress={() => console.log("Image tapped")}>
          <Image style={styles.image} source={require('../assets/images/icon.png')} />
        </TouchableOpacity>
        <Text style= {styles.podTitle}>
          Millennial Investing
        </Text>
        <Text style={styles.title} numberOfLines={1}>
          Episodes
        </Text>
        <SafeAreaView>
          <Button
          title="Episode 15:"
          onPress={() => console.log("Button")}
          color="#fff" />
        </SafeAreaView>
        <SafeAreaView style={{
            backgroundColor: "#626FB2",
            flex: 1,
            //top: 30,
          }}>
        </SafeAreaView>
      </SafeAreaView>

      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      {/* <EditScreenInfo path="/screens/TabOneScreen.js" /> */}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 0.8,
  },
  bars: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    paddingLeft: 10,
    paddingTop: 10,
    fontSize: 15,
    fontWeight: 'bold',
    alignSelf: "flex-start",
    color: "white",
  },
  podTitle: {
    paddingLeft: 0,
    paddingTop: 0,
    fontSize: 15,
    alignSelf: "center",
    color: "white",
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
  image: {
    marginTop: "12%",
    marginBottom: "5%",
    // paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0,
    width: '100%',
    height: 120,
    resizeMode: 'contain',
  },
  center: {
    alignItems: 'center',
  },
  episodebuttons: {
    flex: 0.4,
  }
});
