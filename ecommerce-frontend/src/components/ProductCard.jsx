import { Package, AlertTriangle } from 'lucide-react'

const ProductCard = ({ product }) => {
  const formatPrice = (price) => {
    return new Intl.NumberFormat('es-CO', {
      style: 'currency',
      currency: 'COP',
      minimumFractionDigits: 0,
    }).format(price)
  }

  const getStockStatus = (stock) => {
    if (stock === 0) {
      return { text: 'Agotado', color: 'text-red-600 bg-red-50', icon: true }
    } else if (stock <= 5) {
      return { text: `Stock bajo (${stock})`, color: 'text-orange-600 bg-orange-50', icon: true }
    } else {
      return { text: `En stock (${stock})`, color: 'text-green-600 bg-green-50', icon: false }
    }
  }

  const stockStatus = getStockStatus(product.stock)

  const getTypeColor = (tipo) => {
    const colors = {
      laptop: 'bg-blue-100 text-blue-800',
      monitor: 'bg-purple-100 text-purple-800',
      mouse: 'bg-green-100 text-green-800',
      teclado: 'bg-yellow-100 text-yellow-800',
    }
    return colors[tipo] || 'bg-gray-100 text-gray-800'
  }

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-200">
      <div className="p-6">
        {/* Product Icon */}
        <div className="flex items-center justify-center w-16 h-16 bg-gray-100 rounded-lg mb-4 mx-auto">
          <Package className="w-8 h-8 text-gray-600" />
        </div>

        {/* Product Name */}
        <h3 className="text-lg font-semibold text-gray-900 mb-2 text-center">
          {product.nombre}
        </h3>

        {/* Product Type */}
        <div className="flex justify-center mb-3">
          <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium capitalize ${getTypeColor(product.tipo)}`}>
            {product.tipo}
          </span>
        </div>

        {/* Price */}
        <div className="text-center mb-4">
          <span className="text-2xl font-bold text-gray-900">
            {formatPrice(product.precio)}
          </span>
        </div>

        {/* Stock Status */}
        <div className="flex items-center justify-center">
          <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium ${stockStatus.color}`}>
            {stockStatus.icon && <AlertTriangle className="w-4 h-4 mr-1" />}
            {stockStatus.text}
          </span>
        </div>
      </div>
    </div>
  )
}

export default ProductCard

