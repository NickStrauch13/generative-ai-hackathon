
let savedFileName;


const handleGenerateSteps = async (textValue, setGeneratedSteps, setYoutubeLink) => {
    const url = 'http://127.0.0.1:5000/generate_steps'; 

    const data = {
        query: textValue, 
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const jsonResponse = await response.json();
        setGeneratedSteps(jsonResponse.response);  
        setYoutubeLink(jsonResponse.yt_link);
        savedFileName = jsonResponse.cached_file;
    } catch (error) {
        console.error('Error:', error);
    }
};

export default handleGenerateSteps;
