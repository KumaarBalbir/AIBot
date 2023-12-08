import React, { Component } from "react";
import "../styles/style.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";

class Chatbot extends Component {
  constructor(props) {
    super(props);
    this.state = {
      messages: [],
      userInput: "",
      inputPosition: "5%",
      messageContainerHeight: "auto",
      textEntered: false, // Initially, no text is entered
    };
  }

  handleUserInput = (e) => {
    const userInput = e.target.value;
    this.setState({
      userInput,
      textEntered: userInput.length > 0, // Update the state based on text input
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();

    const userMessage = this.state.userInput;

    this.addMessage("User", userMessage);

    this.setState({ userInput: "" });

    this.sendMessageToBackend(userMessage);
  };

  sendMessageToBackend = (message) => {
    fetch("http://127.0.0.1:5000/chatbot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    })
      .then((response) => response.json())
      .then((data) => {
        this.addMessage("Bot", data.message[0].generated_text);
        this.setState({
          inputPosition: "5%",
          messageContainerHeight: "auto",
          textEntered: false, // Reset textEntered when the message is sent
        });
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  addMessage = (sender, content) => {
    const newMessage = {
      sender,
      content,
    };

    this.setState((prevState) => ({
      messages: [...prevState.messages, newMessage],
    }));
  };

  // Handle key press
  handleKeyPress = (e) => {
    if (e.key === "Enter") {
      this.handleSubmit(e);
    }
  };
  // render() {
  //   return (
  //     <div className="chat-container">
  //       <div className="messages-container" style={{ overflowY: "auto" }}>
  //         {this.state.messages.map((message, index) => (
  //           <div key={index} className={`message ${message.sender}`}>
  //             {message.content}
  //           </div>
  //         ))}
  //       </div>

  //       <div className="input-container" style={{ marginTop: "5%" }}>
  //         <input
  //           type="text"
  //           className="form-control"
  //           placeholder="Type your message"
  //           value={this.state.userInput}
  //           onChange={this.handleUserInput}
  //           onKeyPress={this.handleKeyPress}
  //         />
  //         <button
  //           className={`btn ${
  //             this.state.textEntered ? "btn-success" : "btn-primary"
  //           }`}
  //           onClick={this.handleSubmit}
  //         >
  //           <FontAwesomeIcon icon={faMagnifyingGlass} />
  //           {/* Replace with the icon you want */}
  //         </button>
  //       </div>
  //     </div>
  //   );
  // }

  // Your existing Chatbot component with the updated CSS classes

  render() {
    return (
      <div className="chat-container">
        <div className="messages-container">
          {this.state.messages.map((message, index) => (
            <div key={index} className={`message ${message.sender}`}>
              {message.content}
            </div>
          ))}
        </div>

        <div className="input-container">
          <input
            type="text"
            className="form-control"
            placeholder="Type your message"
            value={this.state.userInput}
            onChange={this.handleUserInput}
            onKeyPress={this.handleKeyPress}
          />
          <button
            className={`btn ${
              this.state.textEntered ? "btn-success" : "btn-primary"
            }`}
            onClick={this.handleSubmit}
          >
            <FontAwesomeIcon icon={faMagnifyingGlass} />
            {/* Replace with the icon you want */}
          </button>
        </div>
      </div>
    );
  }
}

export default Chatbot;
