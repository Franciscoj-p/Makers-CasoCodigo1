import { Link, useLocation } from 'react-router-dom'
import { Store, BarChart3 } from 'lucide-react'

const Navigation = () => {
  const location = useLocation()

  return (
    <nav className="bg-white shadow-sm border-b">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <h1 className="text-xl font-bold text-gray-900">TechStore</h1>
            </div>
          </div>
          <div className="flex items-center space-x-8">
            <Link
              to="/"
              className={`inline-flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors ${
                location.pathname === '/'
                  ? 'text-blue-600 bg-blue-50'
                  : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'
              }`}
            >
              <Store className="w-4 h-4 mr-2" />
              Tienda
            </Link>
            <Link
              to="/dashboard"
              className={`inline-flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors ${
                location.pathname === '/dashboard'
                  ? 'text-blue-600 bg-blue-50'
                  : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'
              }`}
            >
              <BarChart3 className="w-4 h-4 mr-2" />
              Dashboard
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navigation

