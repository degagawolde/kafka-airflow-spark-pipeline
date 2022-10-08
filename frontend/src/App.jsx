import "./app.css";
import RecorderControls from "./components/recorder-controls";
import RecordingsList from "./components/recordings-list";
import useRecorder from "./hooks/useRecorder";

function App() {
  const { recorderState, ...handlers } = useRecorder();
  const { audio } = recorderState;

  return (
    <div className="flex flex-col space-y-10 items-center py-10 h-screen bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 ">
      <div className=" h-3/4 w-3/4 text-white items-center text-center rounded-2xl bg-gradient-to-r from-[#41295a] to-[#2f0743] shadow-md bg-clip-padding backdrop-filter backdrop-blur-sm bg-opacity-10">
        <h1 className="text-4xl p-10">Text Transcription</h1>
        <p className="px-10" >
          here goes the text to read Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
          Asperiores fugit repudiandae ipsa praesentium quaerat magni, rem optio eaque dolores quod fuga 
          voluptatum assumenda fugiat illum laudantium minus magnam harum dolore. Lorem ipsum, dolor sit amet 
          consectetur adipisicing elit. Blanditiis a quibusdam consequuntur id excepturi corporis veniam deserunt tempora, 
          nemo consectetur facilis sapiente temporibus veritatis, dignissimos, sint numquam harum reprehenderit asperiores!
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Autem quas cupiditate laboriosam vero impedit. 
          Autem voluptatum iusto expedita, molestiae consequuntur itaque id alias quibusdam. Eaque, accusantium! Sunt minima recusandae labore! 
        </p>
      </div>
      <div className="justify-center items-center mb-10 shadow-md ">
        <div className="recorder-container">
          <RecorderControls recorderState={recorderState} handlers={handlers} />
          <RecordingsList audio={audio} />
        </div>
      </div>
    </div>
  );
}

export default App;
