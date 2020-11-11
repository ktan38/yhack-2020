import * as React from 'react';
import { StyleSheet, Image, TouchableOpacity, SafeAreaView, Button, Platform, StatusBar } from 'react-native';


import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';

export default function TabOneScreen() {
  return (
    <SafeAreaView style={styles.container}>
      <SafeAreaView style={{
        backgroundColor: "#626FB2",
        flex: 0.2,
        alignItems: 'center'
      }}>
      </SafeAreaView>
      <SafeAreaView style={{
        backgroundColor: "#565EB2",
        flex: 0.4,
        alignItems: 'center'
      }}>
        <TouchableOpacity onPress={() => console.log("Image tapped")}>
          <Image style={styles.image} source={require('../assets/images/icon.png')} />
        </TouchableOpacity>
        <Text style= {styles.podTitle}>
          Millennial Investing
        </Text>
        <Text style= {styles.podDes}>
          By the investor's podcast network 
        </Text>
      </SafeAreaView>
      <SafeAreaView style={{
            backgroundColor: "#626FB2",
            flex: 0.5,
            alignItems: 'center'
          }}>
        <Text style={styles.title} numberOfLines={1}>
          Episodes
        </Text>
        <TouchableOpacity
          activeOpacity={.8} //The opacity of the button when it is pressed
          style = {styles.button}
          onPress={() => console.log("Button")}
        >
        <Image style={styles.play} source={require('../assets/images/Play.png')} />
        <Text style = {{
          color: "white",
          fontWeight: 'bold',
          paddingTop: "10%",
          paddingRight: "38%",
          fontSize: 13,
        }}>
          Episode 15: 
        </Text>
        <Text style = {{
          color: "white",
          fontSize: 9,
          paddingLeft: "8%",
        }}>
          Owning your dream through side hustles and Entrepreneurship with Neil Patel 
        </Text>
        </TouchableOpacity>
      </SafeAreaView>
      {/* <EditScreenInfo path="/screens/TabOneScreen.js" /> */}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  bars: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    paddingLeft: "3%",
    paddingTop: "3%",
    fontSize: 13,
    fontWeight: 'bold',
    alignSelf: "flex-start",
    color: "white",
    marginLeft: "10%",
  },
  podTitle: {
    fontSize: 13,
    fontWeight: 'bold',
    alignSelf: "center",
    color: "white",
  },
  podDes: {
    fontSize: 11,
    alignSelf: "center",
    color: "white",
  },
  image: {
    marginTop: "12%",
    marginBottom: "3%",
    width: 130,
    height: 130,
    resizeMode: 'contain',
    borderRadius: 130/7,
  },
  center: {
    alignItems: 'center',
  },
  button : {
    borderRadius: 100/9,
    width: "75%",
    height: "30%",
    marginTop: "4%",
    marginBottom: "4%",
    backgroundColor: "#82A7C2",
    alignItems: 'center',
    shadowColor: 'rgba(0,0,0, .4)', 
    shadowOffset: { height: 1, width: 1 }, 
    shadowOpacity: 2,
    shadowRadius: 2, 
  },
  play: {
    opacity: "10%",
    width: 20,
    height: 20,
    resizeMode: 'contain',
  },
});
