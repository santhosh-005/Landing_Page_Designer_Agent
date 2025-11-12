import React, { useState } from 'react';

const spaceImages = [
  {
    id: 1,
    src: 'https://images.unsplash.com/photo-1506443432602-ac2fcd6f54e0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80',
    alt: 'Pillars of Creation in the Eagle Nebula',
    title: 'Pillars of Creation',
  },
  {
    id: 2,
    src: 'https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2071&q=80',
    alt: 'A vibrant purple and blue nebula',
    title: 'Cosmic Reef',
  },
  {
    id: 3,
    src: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2072&q=80',
    alt: 'Earth viewed from space at night',
    title: 'Nightfall on Earth',
  },
  {
    id: 4,
    src: 'https://images.unsplash.com/photo-1543722530-d2c3201371e7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2074&q=80',
    alt: 'The Andromeda Galaxy against a starry background',
    title: 'Andromeda Galaxy',
  },
  {
    id: 5,
    src: 'https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2072&q=80',
    alt: 'A satellite orbiting the Earth',
    title: 'Orbital View',
  },
  {
    id: 6,
    src: 'https://images.unsplash.com/photo-1462331940025-496dfbfc7564?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2127&q=80',
    alt: 'A swirling galaxy with a bright core',
    title: 'Spiral Dance',
  },
  {
    id: 7,
    src: 'https://images.unsplash.com/photo-1502134249126-9f3755a50d78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
    alt: 'Colorful gas clouds of the Orion Nebula',
    title: 'Orion\'s Veil',
  },
  {
    id: 8,
    src: 'https://images.unsplash.com/photo-1444703686981-a3abbc4d42e6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
    alt: 'The Milky Way galaxy stretching across a dark night sky',
    title: 'Milky Way Arch',
  },
  {
    id: 9,
    src: 'https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80',
    alt: 'Close up of a star cluster in deep space',
    title: 'Star Cluster',
  },
  {
    id: 10,
    src: 'https://images.unsplash.com/photo-1504333638930-c8787321eee0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
    alt: 'An astronaut floating in space above Earth',
    title: 'The Spacewalker',
  },
  {
    id: 11,
    src: 'https://images.unsplash.com/photo-1529788325122-8a9a2712a329?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
    alt: 'Red planet Mars with its polar ice cap visible',
    title: 'The Red Planet',
  },
  {
    id: 12,
    src: 'https://images.unsplash.com/photo-1570284613060-766c33850e00?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
    alt: 'A beautiful blue and pink nebula',
    title: 'Celestial Bloom',
  },
];

const StarIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.539 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.196-1.539-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.783-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
    </svg>
);


const StellarGallery = () => {
  const [visibleImages, setVisibleImages] = useState(8);

  const loadMoreImages = () => {
    setVisibleImages((prev) => prev + 4);
  };

  return (
    <div className="bg-white text-gray-900 font-sans">
      {/* Header */}
      <header className="absolute top-0 left-0 right-0 z-10 bg-transparent">
        <div className="max-w-7xl mx-auto px-6 lg:px-8">
            <div className="flex justify-between items-center h-20">
                <div className="flex items-center space-x-2">
                    <StarIcon />
                    <span className="text-xl font-bold">Stellar</span>
                </div>
                <nav className="hidden md:flex space-x-8">
                    <a href="#" className="hover:text-pink-500 transition-colors">Discover</a>
                    <a href="#" className="hover:text-pink-500 transition-colors">Gallery</a>
                    <a href="#" className="hover:text-pink-500 transition-colors">Missions</a>
                </nav>
            </div>
        </div>
      </header>

      <main>
        {/* Hero Section */}
        <section className="relative bg-gray-100 h-screen flex items-center justify-center text-center">
            <div 
                className="absolute inset-0 bg-cover bg-center opacity-40" 
                style={{backgroundImage: "url('https://images.unsplash.com/photo-1454789548928-9efd52dc4031?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1780&q=80')"}}>
            </div>
            <div className="relative max-w-7xl mx-auto px-6 lg:px-8">
                <h1 className="text-5xl md:text-7xl font-bold text-gray-900 leading-tight">Journey Through the Cosmos</h1>
                <p className="mt-6 text-lg leading-relaxed max-w-2xl mx-auto">
                    Explore the universe's most stunning vistas, from distant galaxies to the intricate beauty of nebulae. Your adventure into the stars begins now.
                </p>
                <div className="mt-10">
                    <a href="#gallery" className="bg-blue-600 text-white font-bold py-3 px-8 rounded-full text-lg hover:bg-blue-700 transition-transform transform hover:scale-105">
                        Begin Exploration
                    </a>
                </div>
            </div>
        </section>

        {/* Gallery Section */}
        <section id="gallery" className="py-16">
          <div className="max-w-7xl mx-auto px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-4xl font-bold">Stellar Gallery</h2>
              <p className="mt-4 text-lg leading-relaxed text-gray-600">
                A curated collection of breathtaking space photography.
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
              {spaceImages.slice(0, visibleImages).map((image) => (
                <div key={image.id} className="group relative overflow-hidden rounded-lg shadow-lg cursor-pointer">
                  <img
                    src={image.src}
                    alt={image.alt}
                    className="w-full h-full object-cover aspect-square transition-transform duration-500 ease-in-out group-hover:scale-110"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                  <div className="absolute bottom-0 left-0 p-4 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
                      <h3 className="text-white text-lg font-bold">{image.title}</h3>
                  </div>
                </div>
              ))}
            </div>

            {visibleImages < spaceImages.length && (
              <div className="mt-12 text-center">
                <button
                  onClick={loadMoreImages}
                  className="bg-pink-500 text-white font-bold py-3 px-8 rounded-full text-lg hover:bg-pink-600 transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:ring-opacity-50"
                >
                  Load More Wonders
                </button>
              </div>
            )}
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="bg-gray-100">
        <div className="max-w-7xl mx-auto py-12 px-6 lg:px-8">
            <div className="text-center text-gray-500">
                <p>&copy; {new Date().getFullYear()} Stellar Gallery. All rights reserved.</p>
                <p className="mt-2 text-sm">Discover the universe, one photo at a time.</p>
            </div>
        </div>
      </footer>
    </div>
  );
};

export default StellarGallery;
