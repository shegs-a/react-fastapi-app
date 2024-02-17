import logo from './logo.svg';
import './App.css';
import { ChakraProvider } from '@chakra-ui/react';

import Header from "./components/Header"
import Blogs from "./components/ListBlog"
function App() {
  return (
  <ChakraProvider>
    <Header />
    <Blogs />
  </ChakraProvider>
  );
}

export default App;
