import axios from "axios";

export function deleteAudio(audioKey, setRecordings){
    setRecordings((prevState) => prevState.filter((record) => record.key !== audioKey));
}

export async function sendAudio(audioKey, recordings, setRecordings){
    const audio = recordings.find(record => record.key === audioKey );
    setRecordings((prevState) => prevState.filter((record) => record.key !== audioKey));
    console.log("audo", audio);
    // const data = new FormData();
    // const config = {
    //     headers: {
    //         'Content-Type': 'multipart/form-data; boundary=${data._boundary}'
    //     }
    // };

//   try {
//     var formData = new FormData();
//     formData.append('audio', audio.blob);

//     const res = await axios.post('http://localhost:8888/submit', formData, config);
//     console.log(res);
//   } catch (err) {
//     console.log(err.response.data.errors);
//   }
}