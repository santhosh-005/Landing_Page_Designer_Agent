import React from 'react';

const CosmicWonders = () => {
  const wondersData = [
    {
      id: 1,
      title: 'Latest Discoveries',
      description: 'Explore the newest findings from the James Webb Telescope, revealing the universe in unprecedented detail.',
      imageUrl: 'https://images.unsplash.com/photo-1639749594279-9c5953b67b14?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80',
    },
    {
      id: 2,
      title: 'Planet Guides',
      description: 'An in-depth guide to the planets, moons, and mysteries within our own cosmic neighborhood.',
      imageUrl: 'https://images.unsplash.com/photo-1614726353900-9538285b9b78?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1843&q=80',
    },
    {
      id: 3,
      title: 'Stunning Nebulae',
      description: 'Witness the breathtaking beauty of stellar nurseries where new stars are born in vibrant cosmic clouds.',
      imageUrl: 'https://images.unsplash.com/photo-1504333638930-c8787321eee0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80',
    },
  ];

  return (
    <section className="bg-white text-gray-900 py-16">
      <div className="max-w-7xl mx-auto px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-base font-semibold text-blue-600 tracking-wider uppercase">Explore the Universe</h2>
          <p className="mt-2 text-4xl font-bold tracking-tight sm:text-5xl">
            Journey Through Cosmic Wonders
          </p>
          <p className="mt-6 max-w-2xl mx-auto text-lg leading-relaxed text-gray-600">
            From distant galaxies to the planets in our solar system, discover the awe-inspiring beauty and mystery of space.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {wondersData.map((wonder) => (
            <div
              key={wonder.id}
              className="group bg-gray-100 rounded-xl overflow-hidden shadow-md hover:shadow-2xl transition-shadow duration-300 ease-in-out"
            >
              <div className="relative">
                <img
                  className="w-full h-60 object-cover transform group-hover:scale-105 transition-transform duration-500"
                  src={wonder.imageUrl}
                  alt={wonder.title}
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
              </div>
              <div className="p-6">
                <h3 className="text-2xl font-bold text-gray-900">{wonder.title}</h3>
                <p className="mt-3 text-base text-gray-700 leading-relaxed">{wonder.description}</p>
                <a
                  href="#"
                  className="mt-4 inline-block font-semibold text-blue-600 group-hover:text-pink-500 transition-colors duration-300"
                >
                  Learn More &rarr;
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default CosmicWonders;
