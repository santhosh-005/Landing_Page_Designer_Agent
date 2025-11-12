import React from 'react';


const JoinOurVoyageCTA = () => {
  return (
    <section className="bg-secondary-color py-16">
      <div className="container-style">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="heading-style text-text-color">
            Stay Ahead of the Cosmos
          </h2>
          <p className="mt-4 body-style text-gray-700">
            Join our cosmic newsletter for an exclusive journey through the stars. Get the latest space news, mission updates, and breathtaking discoveries delivered directly to your inbox.
          </p>
          <form 
            onSubmit={(e) => e.preventDefault()} 
            className="mt-10 max-w-lg mx-auto"
          >
            <div className="flex flex-col sm:flex-row gap-4">
              <label htmlFor="email-address" className="sr-only">
                Email address
              </label>
              <input
                id="email-address"
                name="email"
                type="email"
                autoComplete="email"
                required
                className="w-full px-5 py-3 placeholder-gray-500 text-text-color bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-color focus:border-primary-color sm:text-sm"
                placeholder="Enter your email address"
              />
              <button
                type="submit"
                className="w-full sm:w-auto flex-shrink-0 px-8 py-3 text-base font-semibold text-white bg-accent-color rounded-md shadow-md hover:bg-pink-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-500 transition duration-300 ease-in-out"
              >
                Subscribe
              </button>
            </div>
          </form>
        </div>
      </div>
    </section>
  );
};

export default JoinOurVoyageCTA;
