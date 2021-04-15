import React from 'react'
import { Card } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import Rating from './Rating'

const Movie = ({movie}) => {
    return (
        <Card className="my-3 p-3 rounded">

            <Link to={`/movie/${movie.id}`}>
                <Card.Img src={movie.image} variant='top'/>
            </Link>
            <Card.Body>
            <Link to={`/movie/${movie.id}`}>
                <Card.Title as='div'>
                    <strong>{movie.name}</strong>
                </Card.Title>
            </Link>
            <Card.Text as='div'>
                <Rating value={movie.rating} text={`${movie.numReviews} reviews`} color="black"/>
            </Card.Text>

            <Card.Text as='h3'>
                ${movie.price}
            </Card.Text>
            </Card.Body>
        </Card>
    )
}

export default Movie
