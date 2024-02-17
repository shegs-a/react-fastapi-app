import React, { useEffect, useState } from "react";
import {
    Box,
    Button,
    Flex,
    Input,
    InputGroup,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    Stack,
    Text,
    useDisclosure
} from "@chakra-ui/react";

const BlogContext = React.createContext({
    blogs: [], fetchBlogs: () => {}
})

export default function Blogs() {
    const [blogs, setBlogs] = useState([])
    const fetchBlogs = async () => {
        const api_url = `${process.env.REACT_APP_API_URL}/${process.env.REACT_APP_LESSON_DAY}/list-blogs`
        console.log(api_url)
        const response = await fetch (api_url)
        const blogs = await response.json()
        setBlogs(blogs.data)
    }
    useEffect(() => {
        fetchBlogs()
    }, [])

    return (
        <BlogContext.Provider value={{blogs, fetchBlogs}}>
            <Stack spacing={5}>
                {blogs.map((blog) => (
                    <div>
                        <p>{blog.slug}</p>
                        <p>{blog.summary}</p>
                    </div>
                ))}
            </Stack>
        </BlogContext.Provider>
    )
}
