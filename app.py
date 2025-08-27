import React from 'react';
import { motion } from 'framer-motion';
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { ShoppingBag } from "lucide-react";

export default function NikeStyleLanding() {
  const products = [
    {
      name: "Air Max 270",
      price: "$150",
      image: "https://images.unsplash.com/photo-1606813903134-45c28b953b3f",
    },
    {
      name: "Jordan Retro",
      price: "$200",
      image: "https://images.unsplash.com/photo-1542291026-7eec264c27ff",
    },
    {
      name: "Blazer Mid '77",
      price: "$120",
      image: "https://images.unsplash.com/photo-1595950653171-47c33e5f1d6e",
    },
  ];

  return (
    <div className="bg-gray-50 min-h-screen">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-r from-black to-gray-800 text-white px-8 py-20 flex flex-col items-center justify-center text-center">
        <motion.h1
          initial={{ opacity: 0, y: -50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-5xl font-extrabold mb-4"
        >
          Step Into Style
        </motion.h1>
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5 }}
          className="text-lg max-w-xl"
        >
          Explore our premium sneakers designed for comfort, performance, and unbeatable style.
        </motion.p>
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.7, type: "spring" }}
          className="mt-6"
        >
          <Button size="lg" className="bg-red-500 hover:bg-red-600 text-white font-semibold rounded-full px-8 py-3">
            Shop Now
          </Button>
        </motion.div>
      </section>

      {/* Product Section */}
      <section className="px-8 py-16">
        <h2 className="text-3xl font-bold text-center mb-12">Featured Sneakers</h2>
        <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {products.map((product, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.2 }}
              viewport={{ once: true }}
            >
              <Card className="shadow-xl hover:shadow-2xl transition-all rounded-2xl overflow-hidden">
                <img src={product.image} alt={product.name} className="w-full h-64 object-cover" />
                <CardContent className="p-4 flex flex-col items-center">
                  <h3 className="text-xl font-semibold">{product.name}</h3>
                  <p className="text-lg text-gray-600">{product.price}</p>
                  <Button className="mt-4 bg-black text-white hover:bg-gray-800 rounded-full">
                    <ShoppingBag className="mr-2 h-4 w-4" /> Add to Cart
                  </Button>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Call to Action */}
      <section className="bg-black text-white py-20 text-center">
        <motion.h2
          initial={{ opacity: 0, y: -50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="text-4xl font-bold mb-6"
        >
          Elevate Your Game
        </motion.h2>
        <p className="mb-8 text-lg max-w-2xl mx-auto">
          Experience sneakers that blend cutting-edge design with ultimate comfort.
        </p>
        <Button size="lg" className="bg-red-500 hover:bg-red-600 text-white rounded-full px-8 py-3">
          Explore Collection
        </Button>
      </section>
    </div>
  );
}


