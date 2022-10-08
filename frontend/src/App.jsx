import "./app.css";
import RecorderControls from "./components/recorder-controls";
import RecordingsList from "./components/recordings-list";
import useRecorder from "./hooks/useRecorder";
import { useState ,useEffect } from "react";
import { getText } from "./handlers/get_text";

function App() {
  const { recorderState, ...handlers } = useRecorder();
  const { audio, blob } = recorderState;
  const [text, setText ] = useState();

  useEffect(() => {
    async function getTextData() {
      const textData = await getText();
      setText(textData.body);
    }
    getTextData();
  },[]);

  return (
    <div className="flex flex-col space-y-10 items-center py-10 h-screen bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 ">
      <div className=" h-3/4 w-3/4 text-white items-center text-center rounded-2xl bg-gradient-to-r from-[#41295a] to-[#2f0743] shadow-md bg-clip-padding backdrop-filter backdrop-blur-sm bg-opacity-10">
        <h1 className="text-4xl p-10">Text Transcription</h1>
        {text === null ? <p className="px-10 h-3/4" >
         unable to fetch the text!   
        </p>: <p className="px-10 h-3/4">
          {text}
        </p> }
      </div>
      <div className="justify-center items-center mb-10 shadow-md ">
        <div className="recorder-container">
          <RecorderControls recorderState={recorderState} handlers={handlers} />
          <RecordingsList audio={audio} blob={blob} />
        </div>
      </div>
    </div>
  );
}

export default App;
