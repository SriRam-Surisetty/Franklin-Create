import { useState } from 'react'
import './App.css'

// Mock function to simulate PDF analysis
const simulatePDFAnalysis = async (fileName: string): Promise<string> => {
  // Simulate API delay
  await new Promise(resolve => setTimeout(resolve, 1500))
  
  // Return mock analysis based on filename
  return `📄 **PDF Analysis Report: ${fileName}**

This is a simulated analysis of your PDF document. In a production environment with the Gemini API, this would contain an actual AI-generated summary.

**Key Sections Identified:**
- Introduction and Overview
- Main Content Analysis
- Key Findings and Conclusions

**Summary:**
The document appears to be a comprehensive resource covering multiple topics with detailed explanations and examples. The content is well-structured with clear sections for better readability.

**Suggested Use Cases:**
- Reference material for the covered topics
- Foundation for further research
- Educational resource

**Note:** This is mock data. Enable the Gemini API in your environment variables to get real AI analysis.`
}

function App() {
  const [file, setFile] = useState<File | null>(null)
  const [result, setResult] = useState<string>('')
  const [loading, setLoading] = useState(false)

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0])
    }
  }

  const handleSubmit = async () => {
    if (!file) return
    setLoading(true)
    try {
      // Simulate PDF analysis with mock data
      const analysisResult = await simulatePDFAnalysis(file.name)
      setResult(analysisResult)
    } catch (error) {
      console.error('Error:', error)
      setResult('Error processing the PDF.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="App">
      <h1>Upload PDF to Gemini</h1>
      <input type="file" accept=".pdf" onChange={handleFileChange} />
      <button onClick={handleSubmit} disabled={!file || loading}>
        {loading ? 'Processing...' : 'Analyze PDF'}
      </button>
      {result && (
        <div>
          <h2>Result:</h2>
          <p>{result}</p>
        </div>
      )}
    </div>
  )
}

export default App