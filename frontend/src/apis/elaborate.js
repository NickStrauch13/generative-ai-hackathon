const handleElaborate = async (textValue, setElaborate, setHasElaborated) => {
    const elaborate_url = 'http://127.0.0.1:5000/elaborate_step'; 

    const data = {
        step: textValue, 
    };

    try {
        const response = await fetch(elaborate_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok, BOZO');
        }

        const jsonResponse = await response.json();
        setElaborate(jsonResponse.response);
        setHasElaborated(true);

    }catch (error) {
        console.error('Error:', error);
    }
}

export default handleElaborate;