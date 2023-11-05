function convertToEmbedURL(youtubeLink) {
    console.log("Original Link:", youtubeLink);
    return youtubeLink.replace("watch?v=", "embed/");
}

const handleGenerateSteps = async (textValue, setGeneratedSteps, setYoutubeLink, setDifficulty, setTime, setCost, setStepsAreLoading, setInfoIsLoading, setHasGenerated) => {
    const generatesteps_url = 'http://127.0.0.1:5000/generate_steps'; 
    const difficulty_url = 'http://127.0.0.1:5000/get_difficulty'

    const data = {
        query: textValue, 
    };

    setStepsAreLoading(true);
    setInfoIsLoading(true);

    try {
        const response = await fetch(generatesteps_url, {
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
        console.log("Received yt_link:", jsonResponse.yt_link);
        setGeneratedSteps(jsonResponse.response);  
        setYoutubeLink(convertToEmbedURL(jsonResponse.yt_link));
        console.log("Updated Embed Link:", convertToEmbedURL(jsonResponse.yt_link));
        setStepsAreLoading(false);

        // Call the second api now
        const response2 = await fetch(difficulty_url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        const jsonResponse2 = await response2.json();
        setDifficulty(jsonResponse2.difficulty);
        setTime(jsonResponse2.time);
        setCost(jsonResponse2.cost);
        setInfoIsLoading(false);

        setHasGenerated(true);

    } catch (error) {
        console.error('Error:', error);
    }
};

export default handleGenerateSteps;
