import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import StorePage from './components/StorePage'
import DashboardPage from './components/DashboardPage'
import Navigation from './components/Navigation'
import './App.css'

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Navigation />
        <Routes>
          <Route path="/" element={<StorePage />} />
          <Route path="/dashboard" element={<DashboardPage />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App

