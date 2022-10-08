import logo from './logo.svg';
import './App.css';
import useRecorder from '../hooks/useRecorder';

function App() {
  const { recorderState, ...handlers } = useRecorder();
  const { audio } = recorderState;
  
  return (
    <div className="App">
    </div>
  );
}

export default App;
