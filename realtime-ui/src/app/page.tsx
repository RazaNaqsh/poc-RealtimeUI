"use client";

import { useState, useEffect } from "react";

interface Resource {
  id: number;
  name: string;
}

export default function Home() {
  const [resources, setResources] = useState<Resource[]>([]);
  const [name, setName] = useState("");
  const [showForm, setShowForm] = useState(false);

  // SSE connection

  useEffect(() => {
  // Step 1: Fetch existing resources
  const fetchResources = async () => {
    const res = await fetch("http://localhost:8000/resources/");
    const data = await res.json();
    setResources(data); // populate table
  };
  fetchResources();

  // Step 2: Set up SSE for live updates
  const eventSource = new EventSource("http://localhost:8000/events");
  eventSource.onmessage = (event) => {
    const newResource: Resource = JSON.parse(event.data);
    setResources((prev) => [newResource, ...prev]);
  };

  return () => eventSource.close();
}, []);

  // Submit new resource
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name) return;
    await fetch("http://localhost:8000/resources/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });
    setName("");
    setShowForm(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-4">SSE Resource Demo</h1>

      <button
        onClick={() => setShowForm(true)}
        className="mb-6 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        Add Resource
      </button>

      {/* Form Popup */}
      {showForm && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-40">
          <div className="bg-white p-6 rounded shadow-md w-80">
            <h2 className="text-xl font-semibold mb-4">New Resource</h2>
            <form onSubmit={handleSubmit}>
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Resource name"
                className="w-full mb-4 px-3 py-2 border rounded"
              />
              <div className="flex justify-end gap-2">
                <button
                  type="button"
                  onClick={() => setShowForm(false)}
                  className="px-4 py-2 border rounded"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
                >
                  Save
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Resource Table */}
      <div className="bg-white shadow rounded p-4">
        <h2 className="text-2xl font-semibold mb-4">Resources</h2>
        {resources.length === 0 ? (
          <p className="text-gray-500">No resources yet</p>
        ) : (
          <table className="w-full text-left border">
            <thead>
              <tr className="bg-gray-200">
                <th className="px-4 py-2 border">ID</th>
                <th className="px-4 py-2 border">Name</th>
              </tr>
            </thead>
            <tbody>
              {resources.map((r) => (
                <tr key={r.id} className="border-b">
                  <td className="px-4 py-2 border">{r.id}</td>
                  <td className="px-4 py-2 border">{r.name}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
