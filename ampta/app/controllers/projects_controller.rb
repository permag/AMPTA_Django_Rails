class ProjectsController < ApplicationController
  before_filter :sidenav
  
  def index
    @projects = Project.all # order...: Project.order("id DESC").all
  end

  def show
    @project = Project.find(params[:id])
  end

  def new
    @project = Project.new
    @users = get_users_except_current
  end

  def create
    @users = get_users_except_current
    @project = Project.new(params[:project])
    @project.owner_id = session[:user_id]

    if params[:project][:project_users]
      params[:project][:project_users].each do |id| 
        @project.users << User.find(id)
      end
    end

    respond_to do |format|
      if @project.save
        u = User.find(session[:user_id])
        u.projects << @project
        format.html { redirect_to project_path(@project), :notice => "Project was created." }
      else
        format.html { render :action => "new" }
      end
    end
  end

  def edit
    @project = Project.find(params[:id])
    @users = get_users_except_current
  end

  def update
    @users = get_users_except_current
    @project = Project.find(params[:id])

    respond_to do |format|
      if @project.update_attributes(params[:project])
        format.html { redirect_to project_path(@project), :notice => "Project was updated." }
      else
        format.html { render :action => "edit" }
      end
    end
  end

  def destroy
    @project = Project.find(params[:id])
    @project.destroy

    respond_to do |format|
      format.html { redirect_to home_index_path, :notice => 'Project was deleted.' }
    end
  end

  def get_users_except_current
    current_user = User.find(session[:user_id])
    @users = (current_user.blank? ? User.all : User.find(:all, :conditions => ["id != ?", current_user.id]))
  end

end