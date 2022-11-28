from fastapi import APIRouter
from config.db import db
from schemas.productos import productosEntity, productoEntity
from bson import ObjectId
from models.productos import Producto



productos = APIRouter()

@productos.get("/productos", tags=["Productos"])
def todos_los_productos():
	return productosEntity( db.productos.find() )

@productos.get("/productos/{id}", tags=["Productos"])
def un_producto(id: str):

    return productoEntity((db.productos.find_one({"_id": ObjectId(id)})))





@productos.delete("/productos/{id}", tags=["Productos"])
def eliminar_producto(id: str):

    db.productos.find_one_and_delete( {"_id": ObjectId(id)} )
    return "Se ha eliminado correctamente"





@productos.post("/productos", tags=["Productos"], response_model=Producto)
def agregar_producto( producto: Producto):
    
    id = db.productos.insert_one(dict( producto)).inserted_id
    return  productoEntity((db.productos.find_one({"_id": ObjectId(id)})))








@productos.put("/productos/{id}", tags=["Productos"], response_model=Producto)
def actualizar_producto(id: str, producto: Producto):

    db.productos.find_one_and_update( 
        {"_id": ObjectId(id)},
        {"$set": dict(producto)} 
    )
    return productoEntity((db.productos.find_one({"_id": ObjectId(id)})))