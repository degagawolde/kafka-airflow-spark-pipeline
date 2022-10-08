import { useState, useEffect } from "react";
import { deleteAudio, sendAudio } from "../handlers/recordings-list";
import generateKey from "../utils/generate-key";

export default function useRecordingsList(audio, blob) {
    const [recordings, setRecordings] = useState([]);

    useEffect(() => {
        if (audio){
            setRecordings((prevState) => {
                return [...prevState, { key: generateKey(), audio, blob }];
            });
        }
    },[audio]);

    return {
        recordings,
        sendAudio: (audioKey) => sendAudio(audioKey, recordings, setRecordings),  
        deleteAudio: (audioKey) => deleteAudio(audioKey, setRecordings),
    };
}