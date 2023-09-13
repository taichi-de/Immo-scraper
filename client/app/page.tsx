"use client";

import { Container, Paper, Input, Button, Tabs } from "@mantine/core";
import axios from "axios";
import Link from "next/link";
import { useEffect, useState } from "react";
import { BsSearch } from "react-icons/bs";

export default function Home() {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  useEffect(() => {
    const headers = {
      Accept: "application/json",
      "Access-Control-Allow-Origin": "*",
    };

    axios
      .get("http://localhost:5001", {
        headers: headers,
      })
      .then((res) => {
        setData(res.data);
        console.log("Data: " + res.data);
      })
      .catch((err) => {
        console.error({ err });
      })
      .finally(() => setLoading(false));
  }, []);

  // TODO: add search function

  return (
    <Container py="lg" className="bg-">
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
            <div>
              <ul
                className="flex justify-around mx-auto px-4 text-slate-500"
                style={{ listStyle: "none" }}
              >
                <li className="">Adresse</li>
                <li className="">Miete</li>
                <li className="">Größe</li>
                <li className="">Zimmer</li>
                <li className="">Datum/ Uhrzeit</li>
              </ul>
            </div>
            <Link href="#" className="no-underline">
              <Paper
                shadow="sm"
                radius="md"
                className="flex justify-around bg-slate-50 hover:bg-slate-50/50 text-left py-6 no-underline"
              >
                <p className="">Muenchen</p>
                <p className="">500€</p>
                <p className="">80</p>
                <p className="">2</p>
                <p className="">08.08.2023</p>
              </Paper>
            </Link>
            <Link href="#" className="no-underline">
              <Paper
                shadow="sm"
                radius="md"
                className="flex justify-around bg-slate-50 hover:bg-slate-50/50 text-left py-6 no-underline"
              >
                <p className="">Muenchen</p>
                <p className="">2000€</p>
                <p className="">110</p>
                <p className="">4</p>
                <p className="">11.12.2023</p>
              </Paper>
            </Link>
          </Tabs.Panel>

          <Tabs.Panel value="Kauf" pt="xs" className="my-5">
            <div>
              <ul
                className="flex justify-around mx-auto px-4 text-slate-500"
                style={{ listStyle: "none" }}
              >
                <li className="">Adresse</li>
                <li className="">Miete</li>
                <li className="">Größe</li>
                <li className="">Zimmer</li>
                <li className="">Datum/ Uhrzeit</li>
              </ul>
            </div>
            <Link href="#" className="no-underline">
              <Paper
                shadow="sm"
                radius="md"
                className="flex justify-around bg-slate-50 hover:bg-slate-50/50 text-left py-6 no-underline"
              >
                <p className="">Muenchen</p>
                <p className="">500€</p>
                <p className="">80</p>
                <p className="">2</p>
                <p className="">08.08.2023</p>
              </Paper>
            </Link>
            <Link href="#" className="no-underline">
              <Paper
                shadow="sm"
                radius="md"
                className="flex justify-around bg-slate-50 hover:bg-slate-50/50 text-left py-6 no-underline"
              >
                <p className="">Muenchen</p>
                <p className="">2000€</p>
                <p className="">110</p>
                <p className="">4</p>
                <p className="">11.12.2023</p>
              </Paper>
            </Link>
          </Tabs.Panel>
        </Tabs>
      ) : (
        <p>Kein Datei</p>
      )}
    </Container>
  );
}
