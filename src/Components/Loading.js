import React, { Component } from "react";

const textArray = ['Gathering your data...', 'Reading your data...', 'Sorting your data...', 'Ranking your data...', 'Hey, you have pretty good taste in music...', 'Getting album covers...', 'Finalizing your results...', 'Loading your songs...','**Clinking and clanking noises..**', 'Almost done...']

class Loading extends Component {
  constructor() {
    super();
    this.state = { textIdx: 0, timeoutTries: 0};
  }

  //set timer for text array 
  componentDidMount() {
    this.timeout = setInterval(() => {
      let currentIdx = this.state.textIdx;
      let currentTimeout = this.state.timeoutTries;
      if (currentIdx + 1 < 10){
        this.setState({ textIdx: currentIdx + 1, timeoutTries: 0 });
      }
      else{
        this.setState({ textIdx: 9, timeoutTries: currentTimeout + 1 }); //after all text in array appear, only show the last element
      }
      if (currentTimeout > 7){
        clearInterval(this.timeout); //if last element appears, stop timer, show error
      }
    }, 8000);
  }

  componentWillUnmount() {
    clearInterval(this.timeout);
  }

  render() {
    let textThatChanges = textArray[this.state.textIdx];
    let timeout = this.state.timeoutTries
    return (
      <div>
        {timeout < 7 ? (<h2 className="loading">{textThatChanges}</h2>) :
        (<h2 className="error"> Something went wrong. Refresh and try again.</h2>)}
      </div>
    )
  }
  
}

export default Loading
