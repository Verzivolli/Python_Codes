def export_to_kml(input_workspace, output_workspace):  
    """ 
    This function extracts the feature classes from a geodatabase 
    and converts them to .kmz files directory structure is maintained 
    by folders being created based on the feature dataset. 
    input_workspace ==> Path to a: Geodatabase, Folder which contains 
    Feature Classes or Shapefiles.  (EX: 'H:\GIS DATA\Counties.gdb') 
    output_workspace ==> Path to the location you want the .kmz files 
    to go.  (EX: 'H:\GIS DATA') 
    """  
    # Searches through all sub-directories within the input workspace  
    import os  
    for dirpath, dirnames, filenames in arcpy.da.Walk(input_workspace):  
        for dirname in dirnames:  
            # vars  
            dir_path = os.path.join(dirpath, dirname)  
            arcpy.env.workspace = dir_path  
            fcs = arcpy.ListFeatureClasses()  
            print("Processing Feature Dataset/Folder:{0}\nFeature Classes/Shapefiles:{1}\n".format(dir_path, fcs))  
            arcpy.CreateFolder_management(output_workspace, dirname)  
            suboutput = os.path.join(output_workspace, dirname)  
            count = 0  
            for fc in fcs:  
                print("Converting: {0}".format(fc))  
                count = count + 1  
                layer = 'layer' + fc  
                out_kmz_file = os.path.join(suboutput, fc + '.kmz')  
                layer_output_scale = 0  
                is_composite = 'false'  
                boundary_box_extent = '#'  
                image_size = 1024  
                dpi = 300  
                zvalue = 'CLAMPED_TO_GROUND'  
                arcpy.MakeFeatureLayer_management(fc, layer) # Creates a layer to convert to the .kmz  
                arcpy.LayerToKML_conversion(layer, out_kmz_file, layer_output_scale, is_composite,  
                                            boundary_box_extent, image_size, dpi, zvalue)  
                print("{0} complete\n".format(count))  

export_to_kml(r"F:\Dropbox\Projekte UTS-01\DLDP - Venddepozitime\TempDataAndWork\PolygonSplit", r"F:\Dropbox\Projekte UTS-01\DLDP - Venddepozitime\TempDataAndWork\PolygonSplit\KMZ")  