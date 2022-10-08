export async function startRecording(setRecorderState){
    try {
       const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

        setRecorderState((prevState) => {
            return {
                ...prevState,
                initRecording: true,
                mediaStream: stream,
            };
        });
    } catch (error) {
        console.log(error);
    }
}

//TODO: function sendRecording(recorder)

export function saveRecording(recorder) {
    if(recorder.state !== 'inactive') recorder.stop();
}