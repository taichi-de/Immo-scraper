"use client";

import { Container, Paper, Input, Button, Tabs } from "@mantine/core";
import axios from "axios";
import { useEffect, useState } from "react";
import { BsSearch } from "react-icons/bs";
import { IoLocationSharp } from "react-icons/io5";

type DataType = {
  title: string;
  location: string;
  size: string;
  rooms: string;
  price: string;
  pricePerM2: number;
};

export default function Home() {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState<DataType[]>([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/data")
      .then((res) => {
        setData(res.data);
      })
      .catch((err) => {
        console.error({ err });
      })
      .finally(() => setLoading(false));
  }, []);

  // TODO: add search function

  return (
    <Container py="lg">
      <Paper
        shadow="sm"
        radius="lg"
        className="h-[30%] bg-purple-200 text-center p-14"
      >
        <h1 className="mt-0 text-blue-900">
          In Welcher Stadt suchst du Wohnung?
        </h1>
        <div className="flex justify-center w-[50%] mx-auto">
          <Input icon={<BsSearch />} placeholder="Stadt" />
          <Button color="pink" className="ml-2">
            Suchen
          </Button>
        </div>
      </Paper>
      {loading && <p className="text-blue-900 text-center">Loading...</p>}
      {data ? (
        <Tabs defaultValue="Miete" className="mt-10 mb-5">
          <Tabs.List grow>
            <Tabs.Tab value="Miete">Miete</Tabs.Tab>
            <Tabs.Tab value="Kauf">Kauf</Tabs.Tab>
          </Tabs.List>
          <Tabs.Panel value="Miete" pt="xs" className="my-5">
            {data.slice(0, 5).map((item, i) => (
              <Paper
                shadow="sm"
                radius="md"
                key={i}
                className="grid grid-cols-4 gap-12 bg-slate-50 hover:bg-slate-50/50 mb-4 p-6 no-underline"
              >
                <div className="col-span-1 bg-blue-400 rounded-lg w-[180px] h-[150px]" />
                <div className="col-span-3 ml-4 p-2">
                  <h2 className="text-base m-0 text-gray-800">{item.title}</h2>
                  <div className="flex">
                    <p className="flex mr-5">
                      <IoLocationSharp className="mt-1 mr-1 text-pink-400" />
                      {item.location}
                    </p>
                  </div>
                  <div className="flex">
                    <p className="my-0">{item.price} €</p>
                    <p className="my-0 mx-5">{item.size} m²</p>
                    <p className="my-0">{item.rooms}</p>
                  </div>
                </div>
              </Paper>
            ))}
          </Tabs.Panel>
          <Tabs.Panel value="Kauf" pt="xs" className="my-5">
            {data.slice(6, 10).map((item, i) => (
              <Paper
                shadow="sm"
                radius="md"
                key={i}
                className="grid grid-cols-4 gap-12 bg-slate-50 hover:bg-slate-50/50 mb-4 p-6 no-underline"
              >
                <div className="col-span-1 bg-blue-400 rounded-lg w-[180px] h-[150px]" />
                <div className="col-span-3 ml-4 p-2">
                  <h2 className="text-base m-0 text-gray-800">{item.title}</h2>
                  <div className="flex">
                    <p className="flex mr-5">
                      <IoLocationSharp className="mt-1 mr-1 text-pink-400" />
                      {item.location}
                    </p>
                  </div>
                  <div className="flex text-base">
                    <p className="my-0">{item.price} €</p>
                    <p className="my-0 mx-5">{item.size} m²</p>
                    <p className="my-0">{item.rooms}</p>
                  </div>
                </div>
              </Paper>
            ))}
          </Tabs.Panel>
        </Tabs>
      ) : (
        <p>Kein Datei</p>
      )}
    </Container>
  );
}
