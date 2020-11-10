import * as React from 'react';
import { StyleSheet, TouchableOpacity, Switch } from 'react-native';

import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';
import { Audio } from 'expo-av';

const podcast = require('../audio/An_Unfinished_Election-79105199.mp3');

function Tog() {
  const [isEnabled, setIsEnabled] = React.useState(false);
  const toggleSwitch = () => setIsEnabled(previousState => !previousState);

    return(
      // <View style={styles.container}>
      <Switch
        trackColor={{ false: "#767577", true: "#81b0ff" }}
        thumbColor={isEnabled ? "#f5dd4b" : "#f4f3f4"}
        ios_backgroundColor="#3e3e3e"
        onValueChange={toggleSwitch}
        value={isEnabled}
      />
      /* </View> */
    );
}

export default class App extends React.Component {
  state = {
    sounds: []
  };

  

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

  toggle = new Tog();
  render() {
    // this.load()
    return (
      <View style={styles.container}>
        toggle
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
        <TouchableOpacity onPress={this.unload}>
          <Text style={styles.buttonText}>Unload</Text>
        </TouchableOpacity>
      </View>
      
    );
  }
}

// export default Toggle = () => {
  

//   return (

//   );
// }




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
