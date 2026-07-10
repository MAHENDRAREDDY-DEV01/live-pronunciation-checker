import { useState } from "react";
import axios from "axios";
import "./App.css";
import {Container,Typography,Button,Card,CardContent,CircularProgress,Box,Stack} from "@mui/material";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyze = async () => {
    if (!file) {
      alert("Please select an audio file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData
      );
      console.log(res.data);
      setResult(res.data);
      console.log(res.data);
    } catch (err) {
      console.log(err);
      alert("Something went wrong");
    }

    setLoading(false);
  };

  return (
    <Container maxWidth="md" sx={{ mt: 5 }}>
    <Typography
      variant="h3"
      align="center"
      gutterBottom
      fontWeight="bold"
    >
      🎤 Live Pronunciation Checker
    </Typography>

    <Box textAlign="center" mt={4}>
      <input
        type="file"
        accept="audio/*"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <Button
        variant="contained"
        onClick={analyze}
        disabled={loading}
      >
        Analyze
      </Button>

      {loading && (
        <Box mt={3}>
          <CircularProgress />
        </Box>
      )}
    </Box>
    {result && (
      <div style={{ marginTop: "30px" }}>
        <Card
        sx={{
          mt: 3,
          mb: 3,
          bgcolor: "#1976d2",
          color: "white",
          textAlign: "center",
          borderRadius: 3,
        }}
        >
          <CardContent>
            <Typography variant="h4">
              Score: {result.score}/100
            </Typography>
          </CardContent>
        </Card>
        <Card sx={{ mb: 3, borderRadius: 3 }}>
          <CardContent>
            <Typography variant="h5" gutterBottom>
              Transcript
            </Typography>
            <Typography>
              {result.transcript}
            </Typography>
          </CardContent>
        </Card>

        <h3>Mistakes</h3>
        { Array.isArray(result?.mistakes) && result.mistakes.map((item, index) => (
          <div
          key={index}
          style={{
            border: "1px solid gray",
            padding: "10px",

            marginBottom: "10px",
            borderRadius: "10px",
            textAlign: "left",
          }}
          >
            <p><strong>Word:</strong> {item.word}</p>
            <br />

            <p><strong>Issue:</strong> {item.issue}</p>
            <br />

            <p><strong>Suggestion:</strong> {item.suggestion}</p>
          </div>
        ))}
        </div>
    )}
    </Container>
  );
}

export default App;