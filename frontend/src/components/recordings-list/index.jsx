import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrashAlt, faExclamationCircle, faPaperPlane } from "@fortawesome/free-solid-svg-icons";
import useRecordingsList from "../../hooks/useRecordingsList";
import './styles.css';

export default function RecordingsList({ audio, blob }) {
    const { recordings, deleteAudio, sendAudio } = useRecordingsList(audio, blob);
  
    return (
      <div className="recordings-container">
        {recordings.length > 0 ? (
          <>
            <h1>Your recordings</h1>
            <div className="recordings-list">
              {recordings.map((record) => (
                <div className="record" key={record.key}>
                  <audio controls src={record.audio} />
                  <div className="delete-button-container">
                    <button
                      className="delete-button"
                      title="Delete this audio"
                      onClick={() => deleteAudio(record.key)}
                    >
                      <FontAwesomeIcon icon={faTrashAlt} />
                    </button>
                  </div>
                  <div className="justify-center text-justify align-baseline">
                    <button
                     onClick={() => sendAudio(record.key)}
                     className="w-20 rounded-md bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 hover:bg-gradient-to-l hover:from-indigo-500 hover:via-purple-500 hover:to-pink-500">
                      <span className="p-2">Send</span>
                      <FontAwesomeIcon icon={faPaperPlane} />
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </>
        ) : (
          <div className="no-records">
            <FontAwesomeIcon className="" icon={faExclamationCircle} size="2x" color="#f2ea02" />
            <span>You don't have records</span>
          </div>
        )}
      </div>
    );
  }
  