import * as React from 'react';
import { StyleSheet, TouchableOpacity, Switch, Platform, Button, ActivityIndicator, Image,TextInput, SafeAreaView, Flatlist } from 'react-native';
import ToggleSwitch from 'toggle-switch-react-native';
import { Searchbar } from 'react-native-paper';
import { LinearGradient } from 'expo-linear-gradient';
import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';
import { Audio } from 'expo-av';

const podcast = require('../audio/An_Unfinished_Election-79105199.mp3');


export default class App extends React.Component {
  state = {
    sounds: []
  };

  toggleState = {
    isOnDefaultToggleSwitch: true,
    isOnLargeToggleSwitch: false,
    isOnBlueToggleSwitch: false
  };

  searchState = {
    firstQuery: '',
  };

  onToggle(isOn) {
    console.log("Changed to " + isOn);
  }

  

  load = async () => {
    await Audio.setIsEnabledAsync(true);
    await Audio.setAudioModeAsync({
      // allowsRecordingIOS: true,
      playsInSilentModeIOS: false,
      interruptionModeIOS: Audio.INTERRUPTION_MODE_IOS_DO_NOT_MIX,
      shouldDuckAndroid: true,
      interruptionModeAndroid: Audio.INTERRUPTION_MODE_ANDROID_DO_NOT_MIX,
      playThroughEarpieceAndroid: false,
      staysActiveInBackground: false,
    });
    const soundObj = await Audio.Sound.createAsync(
      podcast,
      { shouldPlay: false },
    );
    this.setState({ soundObj });
    console.log("hi")
  };

  
  

  play = async () => {
    await this.state.soundObj.sound.playAsync();
  };

  pause = async () => {
    await this.state.soundObj.sound.pauseAsync();
    console.log("hi");
  };

  stop = async () => {
    await this.state.soundObj.sound.stopAsync();
  };

  unload = async () => {
    await this.state.soundObj.sound.unloadAsync();
    this.setState({ soundObj: null });
  };

  render() {
    const { firstQuery } = this.searchState;
    return (
      <View style={styles.container}>
        <LinearGradient
        // Background Linear Gradient
        colors={['#565EB2', '#161A39']}
        style={{
          flex: 1,
          alignSelf: 'stretch',
        }}>
        <View
        style = {{
          flex: 0.5,
          backgroundColor: null,
        }}>
          <Searchbar
            style={{marginTop: 60, marginLeft: 20, marginRight: 20}}
            placeholder="Search"
            onChangeText={query => { this.setState({ firstQuery: query }); }}
            value={firstQuery}
          />
        </View>
        <TouchableOpacity onPress={this.load}>
          <Text style={styles.buttonText}>Load</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={this.play}>
          <Text style={styles.buttonText}>Play</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={this.pause}>
          <Text style={styles.buttonText}>Pause</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={this.stop}>
          <Text style={styles.buttonText}>Stop</Text>
        </TouchableOpacity>
        <ToggleSwitch
          label="Listening Mode"
          size="large"
          onColor="#2196F3"
          isOn={this.state.isOnBlueToggleSwitch}
          onToggle={isOnBlueToggleSwitch => {
            this.setState({ isOnBlueToggleSwitch });
            this.onToggle(isOnBlueToggleSwitch);
          }}
        />
        <TouchableOpacity onPress={this.unload}>
          <Text style={styles.buttonText}>Unload</Text>
        </TouchableOpacity>
        
        </LinearGradient>
      </View>
      
    );
  }
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
  buttonText: {
    padding: 10,
    textAlign: "center",
    fontSize: 20,
  },
  toggle: {
    flex: 1,
    alignItems: "flex-end",
    justifyContent: "center"
  }
});
